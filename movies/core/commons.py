from datetime import datetime, date

import pytz
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.dynamic import AppenderQuery
from sqlalchemy.orm.relationships import RelationshipProperty
from werkzeug import Response

import simplejson as json
from pytz import timezone, utc


def new_alchemy_encoder(revisit_self=False, fields_to_exclude=[], fields_to_expand=[]):
    # reference: https://stackoverflow.com/a/10664192 
    _visited_objs = []
    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if revisit_self:
                    if obj in _visited_objs:
                        return None
                    _visited_objs.append(obj)

                # go through each field in this SQLalchemy class
                fields = {}
                for field in [x for x in dir(obj)]:
                    if field in fields_to_exclude:
                        # not including this field
                        continue
                    
                    # finding field type
                    try:
                        prop = obj._sa_class_manager[field].property
                    except KeyError:
                        # neither a ColumnProperty nor RelationshipProperty
                        continue
                    
                    if isinstance(prop, RelationshipProperty):
                        # Do not expand the field if it is lazy loaded and still unwanted
                        if prop.strategy.strategy_opts['lazy'] == True and field not in fields_to_expand:
                            continue
                        
                    val = obj.__getattribute__(field)

                    # evaluating for dynamic relationships    
                    if isinstance(val, AppenderQuery):
                        fields[field] = val.all()
                    else:
                        fields[field] = val
                        
                # a jsonable dict
                return fields
            if isinstance(obj, (datetime, date)):
                if obj.tzinfo is None or obj.tzinfo.utcoffset(obj) is None:
                    data = obj.replace(tzinfo=pytz.utc)
                    return self.default(data)
                else:
                    return obj.isoformat()
            return json.JSONEncoder.default(self, obj)
    return AlchemyEncoder

def jsonify(obj, revisit_self=False, fields_to_exclude=[], fields_to_expand=[]):
    '''
        :param revisit_self
        :param fields_to_exclude unwanted fields 
        :param fields_to_expand lazyloaded desired fields
    '''
    return Response(json.dumps(obj, cls=new_alchemy_encoder(revisit_self, fields_to_exclude, fields_to_expand)), mimetype='application/json')

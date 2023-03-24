import defaultstart
from defaultstart import GetNewId
logger = defaultstart.logger()


newid = GetNewId.new_uuid("BA")

logger.info('test')
logger.info(newid)

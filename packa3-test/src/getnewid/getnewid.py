 #!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Generate new ID as UUID

Usage
----------
python get_new_id.py : direct call as main program to generate any source ID
import get_new_id.py : as part of add_semantic_identification to semantic record into SPHERES repo

Parameters
----------
-s, --source        : Source EX = External Semantic, IN = Internal Semantic, CO = Constructed Semantic,
                      BA = Baseline data, SA = Sample data, SP = SPHERES platform ID, RE = Real data
-c, --count         : Return list of sourceID with requested amount of IDs
-p, --platform      : Platform name or Platfrom environment as prefix (i.e. SPHERES, TST)
-v, --version       : Platform version as prefix (i.e. 0001), 4 digits is suggested minimum

'''
import uuid
import argparse

#from defaultstart import logger
import defaultstart
logger = defaultstart.logger()

# Get new source ID(s)
def new_uuid(source, count=1, platform = False, version = False):
    try:
        response = []
        prefix = ''
        if platform:
            prefix = platform + '-'
        if version:
            prefix += version + '-'
        # generate uuid
        for uuid_count in range(0, count):
            response.append(prefix + ('' if source == 'SP' else source + '-') + (str(uuid.uuid4())[:8] if source == 'SP' else str(uuid.uuid4())))
        logger.info('Generated ' + str(count) + ' IDs')
        return response
    except Exception as e:
        logger.exception(e)

# Execute as main Python file
if __name__ == '__main__':
    logger.info('"get_new_id" executed as "main" code')
    parser = argparse.ArgumentParser(\
                    prog = 'get_new_id',\
                    description = 'Generate new IDs as UUID',\
                    epilog = '_SPHERES_CODE_')
    parser.add_argument('-s', '--source',\
                    help='ID source (EX = External Semantic, IN = Internal Semantic, CO = Constructed Semantic, BA = Baseline data, SA = Sample data), RE = Real data',
                    required=False, choices=['EX', 'IN', 'CO', 'BA', 'SA', 'RE', 'SP'])
    parser.add_argument('-c', '--count', help='Return list of source IDs with requested amount of IDs',\
                    type=int, required=False, default=1)
    parser.add_argument('-p', '--platform', help='Platform name or Platfrom environment as prefix (i.e. SPHERES, TST)',required=False, default=False)
    parser.add_argument('-v', '--version', help='Platform version as prefix (i.e. 0001), 4 digits is suggested minimum',required=False, default=False)
    args = parser.parse_args()

    # call new_uuid function
    response = new_uuid(args.source, int(args.count), args.platform, args.version)

    # print all UUIDs rows
    print('')
    for uuid in response:
        print(uuid)
    print('')

    logger.info('Finished "get_new_id" execution')

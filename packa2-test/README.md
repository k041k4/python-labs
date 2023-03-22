# Generate new ID as UUID


Generate new ID as UUID

Usage

---

python get_new_id.py : direct call as main program to generate any source ID

import get_new_id.py : as part of add_semantic_identification to semantic record into SPHERES repo

Parameters

---

-s, --source        : Source EX = External Semantic, IN = Internal Semantic, CO = Constructed Semantic,

    BA = Baseline data, SA = Sample data, SP = SPHERES platform ID, RE = Real data

-c, --count         : Return list of sourceID with requested amount of IDs

-p, --platform      : Platform name or Platfrom environment as prefix (i.e. SPHERES, TST)

-v, --version       : Platform version as prefix (i.e. 0001), 4 digits is suggested minimum

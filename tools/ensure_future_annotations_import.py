# Copyright 2023-Present MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Ensure that 'from __future__ import annotations' is used in all package files
"""

import glob
import os
import sys

pattern = "from __future__ import annotations"
missing = []
for dirname in ["pymongo", "bson", "gridfs"]:
    for path in glob.glob(f"{dirname}/*.py"):
        if os.path.basename(path) in ["_version.py", "errors.py"]:
            continue
        found = False
        with open(path) as fid:
            for line in fid.readlines():
                if line.strip() == pattern:
                    found = True
                    break
        if not found:
            missing.append(path)

if missing:
    print(f"Missing '{pattern}' import in:")
    for item in missing:
        print(item)
    sys.exit(1)

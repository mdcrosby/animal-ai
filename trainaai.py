import re
import sys
import argparse

from animalai.train.train import main as runAAILearn
from animalai.envs.settings import AAIOptions

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("  This script lets you use AnimalAI with mlagents-learn")
        print("  The first argument should be the relative path to your AnimalAI training config.yml")
        print("  The following arguments should be the same as for using mlagents-learn directly")
        sys.exit()

    aai_opt = AAIOptions.load_config(sys.argv[1])
    sys.argv.pop(1)

    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    
    sys.exit(runAAILearn(aai_opt))
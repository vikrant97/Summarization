#!/bin/bash
#SBATCH -A research
#SBATCH -n 30
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=3G
#SBATCH --time=4-00:00:00
#SBATCH --mail-type=END

module add cuda/8.0
module add cudnn/7-cuda-8.0

source ~/ire-env/bin/activate
#bash ./train.sh config.txt

bash ./test.sh config.txt output/test_final_results
python postscripts/retreive.py output/test_final_results



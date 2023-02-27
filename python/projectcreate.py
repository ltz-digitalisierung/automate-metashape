#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script to create a metashape project, add a correctly named chunk and add photos 

# based on metashape_workflow.py 
# from Derek Young and Alex Mandel
# University of California, Davis
# 2019

import sys
import yaml

# ---- If this is a first run from the standalone python module, need to copy the license file from the full metashape install: from python import metashape_license_setup

## Define where to get the config file (only used if running interactively)
manual_config_file = "/storage/temp/multilevel_test/cfg/cfg_test2djy.yml" #"config/example_dev.yml"
# ---- If not running interactively, the config file should be supplied as the command-line argument after the python script, e.g.: python metashape_workflow.py config.yml


## Load custom modules and config file: slightly different depending whether running interactively or via command line
try:  # running interactively (in linux) or command line (windows)
    from python import metashape_workflow_functions as meta
    from python import read_yaml
except:  # running from command line (in linux) or interactively (windows)
    import metashape_workflow_functions as meta
    import read_yaml

if(sys.stdin.isatty()):
    config_file = sys.argv[1]
else:
    config_file = manual_config_file

## Parse the config file
cfg = read_yaml.read_yaml(config_file)

### Run the Metashape workflow
doc, log, run_id = meta.project_setup(cfg)

meta.enable_and_log_gpu(log, cfg)

if cfg["load_project"] == "":  # only add photos if this is a brand new project, not based off an existing project
    meta.add_photos(doc, cfg)


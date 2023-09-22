# pre-commit-example
Repository to show the pre-commit tool

# install pre-commit
```bashrc
pip install pre-commit
```

# see pre-commit commands
```bashrc
pre-commit --help
```

# create basic .pre-commit-config.yaml file
```bashrc
pre-commit sample-config > .pre-commit-config.yaml
```

# check other default hooks at https://pre-commit.com/hooks.html
- check-json                # Checks JSON files syntax
- check-yaml                # Checks YAML files syntax
- check-toml                # Checks TOML files syntax
- check-merge-conflict      # Checks for files that contain merge conflict strings
- detect-aws-credentials    # Checks for the existence of AWS secrets that you have set up with the AWS CLI
- debug-statements          # Checks for debugger imports and py37+ breakpoint() calls in python source
- requirements-txt-fixer    # Sorts entries in requirements.txt and constraints.txt
- pretty-format-json        # Checks that all your JSON files are "pretty" (keys sorted and indented)

# some other useful hooks
- black                     # Python code formatter
- jupyter-notebook-cleanup  # Removes cell output of .ipynb notebook and some metadata for better security.
- isort                     # Sorts and organizes Python imports

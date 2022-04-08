## Files in this dir:
- **pip-o_2_pip-req.py**: This file converts the `pip list -o > pip_o.txt` file into pip requirements file which updates all your pip packages via
`pip install -r ./update_pip_requirements.txt`.<br>
Note that when you run the update command there will be dependency conflicts which you will have to resolve manually. One way to do that is by commenting out the update of packages which are causing the conflict. <br>
For example: if the update (installation) `ipython==8.0.2` is causing a conflict because some other library wants
`ipython<8`, you can choose to not update ipython to 8.0.2. This can be done by commenting out the ipython line in the
`update_pip_requirements.txt` file like : `# ipython==8.0.2`

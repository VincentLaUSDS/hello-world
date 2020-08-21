# Development Environment Setup
Some quick instructions for getting dev environment setup for Python parts of the pipeline. This will likely change soon as we control environments with Singularity

Install pyenv virtual env
```
$ brew install pyenv-virtualenv
```

Add the following lines to your `~/.bash_profile` file
```
if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi                                       
 if which pyenv-virtualenv-init > /dev/null; then
     eval "$(pyenv virtualenv-init -)";
fi
```

Install python
```
$ pyenv install 3.7.4
```

Create a new virtual environment and activate
```
pyenv virtualenv 3.7.4 interview-prep
pyenv activate interview-prep
```

Install python packages
```
pip install -r requirements.txt
```

# Useful Tips
For creating plots

```
# using the variable axs for multiple Axes
fig, ax_lst = plt.subplots(2, 2)
ax_lst = ax_lst.ravel()

# and then you can access each element as something like
# ax = ax_lst[0]
```
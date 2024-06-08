
# Speed up your Python code 60x

This repo contains the code examples described in the article [*"Speed up your Python code 60x".*](https://adamcseresznye.github.io/blog/posts/speed_up_py/speed_up_py.html)


## Documentation

- The sequence of modifications made to accelerate the algorithm is documented in the files from PE50_v0.py to PE50_v3.py. 

PE50_v0.py represents the initial code, which is purely Python, while PE50_v3.py has the final version where all functions have been substituted with their Rust equivalents.

- The [**logs**](https://github.com/adamcseresznye/speed_up_py/tree/main/logs) directory contains the recorded execution times.
- The Rust functions are contained in the [**rs_extension.rs**](https://github.com/adamcseresznye/speed_up_py/blob/main/rs_extension.rs).
- The Python Dynamic Module, [**rs_extension.cp310-win_amd64.pyd**](https://github.com/adamcseresznye/speed_up_py/blob/main/rs_extension.cp310-win_amd64.pyd), is the compiled code that is called from our primary function.
## Acknowledgements

 - [rustimport](https://github.com/mityax/rustimport)



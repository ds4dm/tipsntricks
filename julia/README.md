# Introduction to Julia and JuMP

## Installing Julia

### On your machine 
Installation instructions for Julia are found [here](https://julialang.org/downloads/).
On this page you will find:
* Binaries for the current stable release of Julia (v1.2 as of October 16th, 2019)
* Binaries for the long-term support (LTS) release (v1.0 as of October 16th, 2019)

Julia is open-source; the source code can be downloaded [here](https://github.com/JuliaLang/julia).
Instructions for building Julia from source are also found there.

### On GERAD/CIRRELT computers

Julia is already installed on GERAD/CIRRELT computers.
First load the corresponding module, then launch julia normally:
```bash
module load julia
julia
```

Further instructions are found [here](https://www.gerad.ca/aide/doku.php?id=en:programmation-julia).

## Workshop material

The workshop material can be found [here](https://github.com/ds4dm/tipsntricks/tree/julia).
To download the material, either
* clone the repository locally and checkout the `julia` branch
```bash
git clone https://github.com/ds4dm/tipsntricks
cd tipsntricks
git checkout julia
```
* download [the zipped repository](https://github.com/ds4dm/tipsntricks/archive/julia.zip) and uncompress it locally.

The material is in the `julia/` folder.

## Jupyter notebooks

You can run Julia within Jupyter notebooks.
To do so, you will need to install the [IJulia package](https://github.com/JuliaLang/IJulia.jl).
See the link for installation instructions.

If you already have Jupyter installed (e.g. with Anaconda), you should see a Julia kernel within Jupyter.
If not, Julia will download and install its own conda distribution, and you will have to launch Jupyter from within Julia.

## JuMP tutorials

During the workshop, we will present you our JuMP
tutorials (based on `Facily location` and `Asymmetric travelling salesman` problems) and some tutorials of `JuMPTutorials.jl` like a Sudoku.
As of October 18th, look to [JuMPTutorials package](https://github.com/amontoison/JuMPTutorials.jl) for more examples that work with JuMP 0.20.0 and Julia 1.2/1.3. You can run their notebooks directly from the web browser without any installation!

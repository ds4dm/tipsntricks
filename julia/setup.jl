@info "Installing packages. This may take up to a few minutes."

using Pkg
Pkg.activate(".")
Pkg.instantiate()

@info "Loading packages"

# Standard packages
using Random
using Printf
using Test
using DelimitedFiles

using JuMP
const MOI = JuMP.MathOptInterface

using GLPK
using Cbc

using LinearAlgebra
using SparseArrays

@info "All packages successfully imported."

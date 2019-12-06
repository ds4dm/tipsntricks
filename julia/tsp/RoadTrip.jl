function RoadTrip(N, c, sol)
cities_visited = 1
city = 1
println(c[city])
while cities_visited ≠ N
    city = findfirst(sol[city,:] .== 1.0) 
    cities_visited += 1
    println(c[city])
end
end
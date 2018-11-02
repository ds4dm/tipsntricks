# 
function f1() 
    sleep(0.01)  # sleep for 10ms
    return 0
end
function f2()
    sleep(0.005)  # sleep for 1ms
    return 0
end

function g1()
    sleep(0.001)  # sleep for 1ms
end
function g2()
    sleep(0.05)  # sleep for 10ms
end

# Simulate the outer loop
function h1()
    for i in 1:100
        f1()
        g1()
    end
    println("100 iterations")
    return 0
end

function h2()
    for i in 1:20
        f2()
        g2()
    end
    println("20 iterations")
    return 0
end
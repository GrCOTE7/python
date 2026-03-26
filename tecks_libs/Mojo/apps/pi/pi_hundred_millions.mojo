from python import Python

fn pi(n: Int) -> Float64:
    var total: Float64 = 0.0
    for i in range(1 - 2 * n, 2 * n + 1, 4):
        total += 1.0 / i
    return 4.0 * total

fn main() raises:
    var time_mod = Python.import_module("time")
    var empty_tuple = Python.tuple()
    var start_time = time_mod.call_method("time", empty_tuple)

    print(pi(100_000_000))

    var end_time = time_mod.call_method("time", empty_tuple)
    var elapsed = end_time - start_time
    print("Time: ", elapsed, "s")

# Declare a wrapper function that can raise
fn run_main() raises:
    main()

# Function to handle exceptions
fn execute() raises:
    try:
        run_main()
    except e:
        print("Une erreur s'est produite : ", e)

# Call the function that handles exceptions
try:
    execute()
except e:
    print("Une erreur s'est produite lors de l'exécution : ", e)

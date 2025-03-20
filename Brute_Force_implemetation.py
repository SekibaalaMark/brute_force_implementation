# Adjacency list representation of the graph
# Each key is a node, and the value is a dictionary of connected nodes with their respective distances
adjacency_list = {
    1: {2: 12, 3: 10, 7: 12},
    2: {1: 12, 3: 8, 4: 12},
    3: {1: 10, 2: 8, 4: 11, 5: 3, 7: 9},
    4: {2: 12, 3: 11, 5: 11, 6: 10},
    5: {3: 3, 4: 11, 6: 6, 7: 7},
    6: {4: 10, 5: 6, 7: 9},
    7: {1: 12, 3: 9, 5: 7, 6: 9}
}

def generate_permutations(nodes):
    """Generate all permutations of a list of nodes.
    
    Argument:
        nodes (list): A list of nodes to permute.
    
    Returns:
        list: A list of all possible permutations of the input nodes.
    """
    if len(nodes) == 1:
        return [nodes]  # Base case: only one node, return it as the only permutation
    
    permutations = []  # List to store all permutations
    for i in range(len(nodes)):
        node = nodes[i]  # Select the current node
        remaining_nodes = nodes[:i] + nodes[i+1:]  # Remaining nodes after removing the current node
        
        # Recursively generate permutations of the remaining nodes
        for perm in generate_permutations(remaining_nodes):
            permutations.append([node] + perm)  # Append the current node to each permutation of the remaining nodes
            
    return permutations

def generate_valid_sequences():
    """
    Generate all valid permutations of nodes 2-7 and prepend + append node 1
    to ensure cycles start and end at node 1 (the starting point).
    
    Returns:
        list: A list of valid sequences representing possible tours.
    """
    nodes = ["2", "3", "4", "5", "6", "7"]  # Nodes to permute (excluding the starting node 1)
    
    # Generate permutations and format them to start and end with node 1
    perm_list = ['1' + ''.join(p) + '1' for p in generate_permutations(nodes)]
    return perm_list

# Generate all valid sequences (tours) starting and ending at node 1
sequences = generate_valid_sequences()
results = {}  # Dictionary to store valid routes and their total distances

# Compute distances for each valid route
for sequence in sequences:
    total_distance = 0  # Initialize total distance for the current route
    valid = True  # Track validity of the path

    # Iterate through the sequence to calculate the total distance
    for i in range(len(sequence) - 1):
        current_node = int(sequence[i])  # Current node in the sequence
        next_node = int(sequence[i + 1])  # Next node in the sequence

        # Check if there is a valid connection between the current and next node
        if next_node in adjacency_list[current_node]:
            total_distance += adjacency_list[current_node][next_node]  # Add the distance to the total
        else:
            valid = False  # Mark the route as invalid if no connection exists
            break  # Stop checking if an invalid connection is found

    # If the route is valid, store it in the results dictionary
    if valid:
        results[sequence] = total_distance  # Map the sequence to its total distance

# Find the best (shortest) route from the results
best_route = min(results, key=results.get)  # Get the route with the minimum distance
print(f"Final Tour: {best_route}")  # Output the best route
print(f"Total route cost is {results[best_route]}")#Output the total distance covered in the best route tour
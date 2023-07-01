def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []
    else:
        # Create an empty list to hold each row of the triangle
        triangle = []
        for i in range(n):
            # Create a new list for each row
            row = []
            for j in range(i+1):
                # Calculate the value of each element in the row
                if j == 0 or j == i:
                    row.append(1)
                else:
                    """Each element is the sum of the two elements
                    above it in the previous row"""
                    row.append(triangle[i-1][j-1] + triangle[i-1][j])
            # Append the row to the triangle list
            triangle.append(row)
        # Print the triangle
        return triangle

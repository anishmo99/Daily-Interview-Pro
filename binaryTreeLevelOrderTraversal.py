def levelOrder(self, root):
		# Use a queue to keep track of the node and it's depth in the tree
        q = deque([(root, 0)])
		# Dictionary to keep track of the the values at each depth
        results = {}
		
        while q:
            node, i = q.popleft()
			# If this is the first visit to this depth set to empty list
            if i not in results:
                results[i] = []
            if node:
			    # Add each value to it's corresponding list within the dictionary
                results[i].append(node.val)
				# Add the left and right value to the queue and increment the depth
                q.append((node.left, i+1))
                q.append((node.right, i+1))
				
        # List comprehension to change the Dictionary of lists to a list of lists
        return [results[key] for key in results if results[key]]
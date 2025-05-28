#!/usr/bin/node

// Get all arguments starting from index 2 (after node and script name)
const args = process.argv.slice(2);

// If no arguments or only one argument, print 0
if (args.length <= 1) {
  console.log(0);
} else {
  // Convert all arguments to integers
  const nums = args.map(arg => parseInt(arg));

  // Sort in descending order
  nums.sort((a, b) => b - a);

  // Print the second element (second biggest)
  console.log(nums[1]);
}

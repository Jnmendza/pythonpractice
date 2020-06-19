What is Big O notation?

We need a way to talk about efficiency (number of operations in the worst case) in a more general sense.

Big O notation is a way of describing the rate of change in the execution speed of an algorithm when the 
data size increases. It is the agreed-upon terminology we use to describe how long an algorithm takes to run.
It is a way of comparing different algorithm’s efficiencies.

The specific terms of Big O notation describe how fast the runtime grows (relative to the size of the input) 
with a focus on when the input gets extremely large.

We also talk about runtime relative to the input size because we need to express our speed in terms of something. 
So we show the speed of the algorithm in terms of the input size. That way, we can see how the speed reacts as the 
input size grows.


Common Big O run times
https://learn.lambdaschool.com/cs/module/rec3MaMAY78iDm7ax/


n represents the size of the data

Constant Time O(1):
def print_one_item(items):
    print(items[0])
    
No matter how large or small the input is (1,000,000 or 10), the number of computations with the function is the same
    

Linear Time O(n):
def print_every_item(items):
    for item in items:
        print(item)
        
The speed of the algorithms increase at the same rate as the input size. If items has ten items, then the 
function will print ten times. If it has 10,000 items, then the function will print 10,000 times.


Quadratic Time O(n^2):
def print_pairs(items):
    for item_one in items:
        for item_two in items:
            print(item_one, item_two)
            
Why is this quadratic time? The clue is nested for loops. These nested for loops means that for each item in items
(the outer loop), we iterate through every item in items(the inner loop). For an input size of n, we have to print 
n * n times or n^2 times.


Quiz ______
def do_a_bunch_of_stuff(items):
    last_idx = len(items) -1
    print(items[last_idx])
    
    middle_idx = len(items) / 2
    idx = 0
    while idx < middle_idx:
        print(items[idx])
        idx = idx + 1
        
    for num in range(2000):
        print(num)
        
        
print(items[last_idx]) is constant time because it doesn’t change as the input changes. So, that portion of the function is O(1).

The while loop that prints up to the middle index is 1/2 of whatever the input size is; we can say that portion of the function is O(n/2).

The final portion will run 2000 times, no matter the size of the input.

So, putting it all together, we could say that the efficiency is O(1 + n/2 + 2000). However, we don’t say this. We just describe 
this function as having linear time O(n) because we drop all of the constants. Why do we cut all of the constants? 
Because as the input size gets huge, adding 2000 or dividing by 2 has minimal effect on the performance of the algorithm.


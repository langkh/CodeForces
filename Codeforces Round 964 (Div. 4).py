def sum_of_digits(n):
    return (n // 10) + (n % 10)

# Read the number of test cases
t = int(input().strip())

# Process each test case
for _ in range(t):
    n = int(input().strip())
    print(sum_of_digits(n))






def count_suneet_wins(a1, a2, b1, b2):
    #suneet_cards = [a1, a2]
    #slavic_cards = [b1, b2]
    
    win_count = 0
    
    outcomes = [
        (a1, b1, a2, b2),
        (a1, b2, a2, b1),
        (a2, b1, a1, b2),
        (a2, b2, a1, b1)
    ]
    
    for (s1, l1, s2, l2) in outcomes:
        if s1 > l1 and s2 > l2:
            win_count += 1
        elif s1 > l1 and s2 <= l2:
            win_count += 1
        elif s1 <= l1 and s2 > l2:
            win_count += 1
    
    return win_count

def main():
    t = int(input().strip())
    results = []
    
    for _ in range(t):
        a1, a2, b1, b2 = map(int, input().strip().split())
        results.append(count_suneet_wins(a1, a2, b1, b2))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()




def count_suneet_wins(a1, a2, b1, b2):
    #suneet_cards = [a1, a2]
    #slavic_cards = [b1, b2]
    
    win_count = 0
    
    # All possible outcomes
    outcomes = [
        (a1, b1, a2, b2),
        (a1, b2, a2, b1),
        (a2, b1, a1, b2),
        (a2, b2, a1, b1)
    ]
    
    for s1, l1, s2, l2 in outcomes:
        suneet_wins = 0
        slavic_wins = 0
        
        if s1 > l1:
            suneet_wins += 1
        elif s1 < l1:
            slavic_wins += 1
            
        if s2 > l2:
            suneet_wins += 1
        elif s2 < l2:
            slavic_wins += 1
            
        if suneet_wins > slavic_wins:
            win_count += 1
    
    return win_count

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        a1 = int(data[index])
        a2 = int(data[index + 1])
        b1 = int(data[index + 2])
        b2 = int(data[index + 3])
        index += 4
        results.append(count_suneet_wins(a1, a2, b1, b2))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

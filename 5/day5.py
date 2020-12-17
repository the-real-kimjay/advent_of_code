import sys


def main():
    input_lines = get_input()
    max_seat,my_seat = process_passes((input_lines))

    print('Max seat_id = ' + str(max_seat))
    print('My seat_id = ' + str(my_seat))


def process_passes(passes):
    identified_seats = []
    
    for b_pass in passes:
        row = parse_binary(b_pass[:7],'F','B')
        col = parse_binary(b_pass[7:],'L','R')
        seat_id = row * 8 + col
        identified_seats.append(seat_id)

    my_seat = find_seat(identified_seats)

    return max(identified_seats),my_seat
   

def parse_binary(partition,B,E):
    lower = 0
    upper = (2**len(partition)) - 1
    for char in partition:
        if char == B: upper = upper - int((upper-lower+1)/2)
        if char == E: lower = lower + int((upper-lower+1)/2)
    return upper


def find_seat(seats):
    for i,seat in enumerate(seats):
        if seat + 1 not in seats and seat + 2 in seats:
            return (seat + 1)


def get_input(input_file='day5_input.txt'):
    with open (input_file, 'r') as f:
        return [line.rstrip('\n') for line in f]


if __name__ == '__main__':
    main()
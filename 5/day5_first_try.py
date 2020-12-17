import sys


def main():
    input_lines = get_input()
    process_passes((input_lines))


def process_passes(passes):
    # max_seat_id = 0
    # rows = passes[0][:7]
    # cols = passes[0][7:]
    # all_seat_ids = list(range(2**len(cols) * 2**len(rows)))
    # pass_details = {}
    identified_seats = []
    
    for b_pass in passes:
        row = parse_binary(b_pass[:7],'F','B')
        col = parse_binary(b_pass[7:],'L','R')
        seat_id = row * 8 + col
        identified_seats.append(seat_id)
        # pass_details[seat_id] = {'row':row, 'col': col, 'b_pass':b_pass}

        # if seat_id > max_seat_id: max_seat_id = seat_id
        # all_seat_ids.remove(seat_id)

    # my_seat_id = find_seat(all_seat_ids,pass_details)
    my_seat = find_seat(identified_seats)

    print('Max seat_id = ' + str(max(identified_seats)))
    print('My seat_id = ' + str(my_seat))


def parse_binary(partition,B,E):
    lower = 0
    upper = (2**len(partition)) - 1
    for char in partition:
        if char == B: upper = upper - int((upper-lower+1)/2)
        if char == E: lower = lower + int((upper-lower+1)/2)
    return upper


# def find_seat(seats,pass_details):
#     for seat_id in seats:
#         if (seat_id - 1) in pass_details and (seat_id + 1) in pass_details: 
#             return(seat_id)

def find_seat(pass_details):
    for i,seat in enumerate(pass_details):
        if seat + 1 not in pass_details and seat + 2 in pass_details:
            return (seat + 1)



def get_input(input_file='day5_input.txt'):
    with open (input_file, 'r') as f:
        return [line.rstrip('\n') for line in f]

if __name__ == '__main__':
    main()
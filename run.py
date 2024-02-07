from booking.booking import Booking

import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--place_to_go", type=str, help="Place_to_go", required=True)
    parser.add_argument("-i", "--check_in", type=str, help="Check-in date (YYY-MM-DD)", required=True)
    parser.add_argument("-o", "--check_out", type=str, help="Check-out date (YYY-MM-DD)", required=True)
    parser.add_argument("-n", "--nr_adults", type=int, help="Number of adults", required=False, default=1)
    args = vars(parser.parse_args())
    return args

def main():
    args = get_args()

    with Booking() as bot:
        bot.land_first_page()
        # bot.change_currency()
        bot.select_place_to_go(args["place_to_go"]) # works in Debug mode, but not otherwise
        
        bot.select_dates(args["check_in"], args["check_out"])
        bot.select_adults(args["nr_adults"])
        bot.click_search()
        bot.apply_filters() # works in Debug mode, but not otherwise
        bot.report_results()
        print('Exiting...')

if __name__ == "__main__":
    main()


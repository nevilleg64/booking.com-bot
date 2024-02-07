from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    # bot.change_currency()
    bot.select_place_to_go('Albury') # works in Debug mode, but not otherwise
    
    bot.select_dates(check_in='2024-02-19', check_out='2024-02-26')
    bot.select_adults(1)
    bot.click_search()
    bot.apply_filters() # works in Debug mode, but not otherwise
    bot.report_results()
    print('Exiting...')
    


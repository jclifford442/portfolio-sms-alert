import core
import helpers


def main():
    if not helpers.check_file("../sms-stock-alert/files/portfolio_holdings.xlsx"):
        helpers.build_holdings_worksheet()
    if not helpers.check_file("../sms-stock-alert/files/portfolio_history.xlsx"):
        helpers.build_history_worksheet()
    core.daily_gain_amount()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


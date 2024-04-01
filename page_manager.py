
class PageManager:
    @staticmethod
    def show_add_transaction_page(user, user_retrieved):
        from add_transaction import addTransaction
        addTransaction(user, user_retrieved)

    @staticmethod
    def show_user_page(user_retrieved):
        from user_page import userPage
        userPage(user_retrieved)

    @staticmethod
    def show_connection_page():
        from connection_page import connectionPage
        connectionPage()

    @staticmethod
    def show_home_page():
        from home_page import homePage
        homePage()

    @staticmethod
    def show_account_creation_page():
        from account_creation import accountCreation
        accountCreation()

    @staticmethod
    def show_transaction_list_page(user_retrieved):
        from transaction_list import transactionList
        transactionList(user_retrieved)

    @staticmethod
    def show_filter_page(user_retrieved):
        from filter_page import filterPage
        filterPage(user_retrieved)

    @staticmethod
    def show_monthly_recap_page(user_retrieved):
        from monthly_recap_page import monthlyTransactionList
        monthlyTransactionList(user_retrieved)

    @staticmethod
    def show_alerts_page(user_retrieved):
        from alerts_page import alerts
        alerts(user_retrieved)

    @staticmethod
    def show_graphics_page(user_retrieved):
        from graphics_page import transactionGraphics
        transactionGraphics(user_retrieved)

    @staticmethod
    def show_sort_by_date_page(user_retrieved):
        from sort_by_date import sortByDate
        sortByDate(user_retrieved)

    @staticmethod
    def show_sort_by_amount_page(user_retrieved):
        from sort_by_amount import sortByAmount
        sortByAmount(user_retrieved)

    @staticmethod
    def show_sort_by_category_page(user_retrieved):
        from sort_by_category import sortByCategory
        sortByCategory(user_retrieved)

    @staticmethod
    def show_sort_by_type_page(user_retrieved):
        from sort_by_type import sortByType
        sortByType(user_retrieved)

    @staticmethod
    def show_sort_between_two_dates_page(user_retrieved):
        from sort_between_two_dates import sortBetweenTwoDates
        sortBetweenTwoDates(user_retrieved)
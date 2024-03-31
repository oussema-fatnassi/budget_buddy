
class PageManager:
    @staticmethod
    def show_add_transaction_page(user=None):
        from add_transaction import addTransaction
        addTransaction(user)

    @staticmethod
    def show_user_page():
        from user_page import userPage
        userPage()

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
    def show_transaction_list_page():
        from transaction_list import transactionList
        transactionList()

    @staticmethod
    def show_filter_page():
        from filter_page import filterPage
        filterPage()

    @staticmethod
    def show_monthly_recap_page():
        from monthly_recap_page import monthlyTransactionList
        monthlyTransactionList()

    @staticmethod
    def show_alerts_page():
        from alerts_page import alerts
        alerts()

    @staticmethod
    def show_graphics_page():
        from graphics_page import transactionGraphics
        transactionGraphics()
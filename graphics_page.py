import pygame
import pygame_gui
import sys
import database_operation 
from GUI import GUI
from page_manager import PageManager
from plotter import Plotter
import datetime  

def transactionGraphics(retrieved_user):
    gui = GUI()
    window = gui.createWindow("Transaction Graphics")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo =gui.createImage(window, 50, 50, 75, 50, "images/Logo.png")


    choseGraphmenu = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((20, 100), (150, 30)),
        options_list=["Monthly recap", "By category"],
        starting_option="Monthly recap",
        manager=gui.MANAGER,
        object_id="drop_down"
    )

    confirmButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 500), (100, 30)),
        text='CONFIRM',
        manager=gui.MANAGER,
        object_id="confirm_button"
    )
    closeButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 550), (100, 30)),
        text="CLOSE",
        manager=gui.MANAGER,
        object_id="close_button"
    )

    monthList1 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((175, 100), (100, 30)),
        options_list=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        starting_option="January",
        manager=gui.MANAGER,
        object_id="month_list1"
    )
    yearList1 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((275, 100), (100, 30)),
        options_list=["2024","2023","2022","2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"],
        starting_option="2024",
        manager=gui.MANAGER,
        object_id="year_list1"
    )
    graphsLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((70, 50), (300, 30)),
        text="Choose graph type and period",
        manager=gui.MANAGER,
        object_id="label"
    )

    plot_surface = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            gui.MANAGER.process_events(event)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == closeButton:
                        PageManager.show_user_page(retrieved_user)
                    if event.ui_element == confirmButton:
                        if choseGraphmenu.selected_option == "Monthly recap":
                            selected_month = monthList1.selected_option
                            month_number = datetime.datetime.strptime(selected_month, "%B").month
                            selected_year = int(yearList1.selected_option)  # Get the selected year
                            transaction_names, total_income, total_expenses = database_operation.get_monthly_transactions(retrieved_user[0], month_number, selected_year)
                            Plotter.plot_monthly_summary(selected_month, selected_year, total_income, total_expenses)
                            plot_surface = pygame.image.load('plot.png')
                        elif choseGraphmenu.selected_option == "By category":
                            selected_month = monthList1.selected_option
                            month_number = datetime.datetime.strptime(selected_month, "%B").month
                            selected_year = int(yearList1.selected_option)  # Get the selected year
                            categories, amounts = database_operation.get_transactions_by_category_period(retrieved_user[0], month_number, selected_year)
                            if not categories:  # Check if no transactions found
                                categories = []
                                amounts = []
                            Plotter.plot_category_summary(selected_month, selected_year, categories, amounts)
                            plot_surface = pygame.image.load('category_plot.png')

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(uiRefreshRate)
        logo =gui.createImage(window, 50, 50, 75, 50, "images/Logo.png")
 
        if plot_surface:  
            window.blit(plot_surface, (30, 180))  
        gui.MANAGER.draw_ui(window)   
        pygame.display.update()

# if __name__ == "__main__":
#     retrieved_user = None  
#     transactionGraphics(retrieved_user)

import pygame
import pygame_gui
import sys
from GUI import GUI

def userPage():
    gui = GUI()
    window = gui.createWindow("User Page")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo = gui.createImage(window, 50, 50, 50, 50, "images/logo.png")

    logoutButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((325, 25), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="logout_button"
    )
    addTransactionButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 200), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="add_transaction_button"
    )
    transactionListButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((175, 200), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="transaction_list_button"
    )
    filterButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((300, 200), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="filter_button"
    )
    monthlyRecapButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 500), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="monthly_recap_button"
    )
    alertsButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((175, 500), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="alerts_button"
    )
    graphicsButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((300, 500), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="graphics_button"
    )
    lastTransactionsList = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((50, 300), (300, 200)),
        item_list=["Transaction 1", "Transaction 2", "Transaction 3", "Transaction 4", "Transaction 5"],
        manager=gui.MANAGER,
        object_id="selection_list",
        allow_double_clicks=True
    )
    currentAmount = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((100, 80), (200, 100)),
        html_text="100000000 €",
        manager=gui.MANAGER,
        object_id="current_amount_text_box"
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            gui.MANAGER.process_events(event)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_SELECTION_LIST_DOUBLE_CLICKED_SELECTION:
                    if event.ui_element == lastTransactionsList:
                        selected_item = event.text
                        pygame_gui.windows.UIMessageWindow(
                            rect=pygame.Rect((50, 50), (300, 300)),
                            html_message= selected_item,
                            manager=gui.MANAGER,
                            window_title='Message Box',
                            object_id="message_box"
                        )

                elif event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == logoutButton:
                        print("Logout button pressed.")
                    if event.ui_element == addTransactionButton:
                        print("Add transaction button pressed.")
                    if event.ui_element == transactionListButton:
                        print("Transaction list button pressed.")
                    if event.ui_element == filterButton:
                        print("Filter button pressed.")
                    if event.ui_element == monthlyRecapButton:
                        print("Monthly recap button pressed.")
                    if event.ui_element == alertsButton:
                        print("Alerts button pressed.")
                    if event.ui_element == graphicsButton:
                        print("Graphics button pressed.")

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        gui.createImage(window, 50, 50, 50, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    userPage()
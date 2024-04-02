import pygame
import pygame_gui
import sys
from GUI import GUI
from page_manager import PageManager
import database_operation

def alerts(retrieved_user):
    gui = GUI()
    window = gui.createWindow("Alerts Page")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo =gui.createImage(window, 50, 50, 75, 50, "images/Logo.png")
    label = gui.createLabel(window, 50, 150, 300, 50, "Select alert to view details")

    alertsList = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((50, 200), (300, 200)),
        item_list=[],
        manager=gui.MANAGER,
        object_id="alerts_list"
    )
    closeButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 550), (100, 30)),
        text="CLOSE",
        manager=gui.MANAGER,
        object_id="close_button",
        tool_tip_text="Return to the user page"
    )

    alerts_data = database_operation.get_alerts_for_user(retrieved_user[0])
    alert_types = [alert[1] for alert in alerts_data]
    alertsList.set_item_list(alert_types)

# Print the extracted alert types
    print(alert_types)
    # for alert_type in types:
    #     alertsList.add_items(alert_type)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            gui.MANAGER.process_events(event)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_SELECTION_LIST_DOUBLE_CLICKED_SELECTION:
                    if event.ui_element == alertsList:
                        selected_item = event.text
                        transaction_details = database_operation.get_transaction_details(selected_item, retrieved_user[0])
                        if transaction_details:
                            details_text = f"<b>Name:</b> {transaction_details['name']}<br>" \
                               f"<b>Description:</b> {transaction_details['description']}<br>" \
                               f"<b>Amount: € </b> {transaction_details['amount']}<br>" \
                               f"<b>Category:</b> {transaction_details['category']}<br>" \
                               f"<b>Type:</b> {transaction_details['type']}<br>" \
                               f"<b>Date:</b> {transaction_details['date']}"
                        pygame_gui.windows.UIMessageWindow(
                            rect=pygame.Rect((50, 50), (300, 300)),
                            html_message= details_text,
                            manager=gui.MANAGER,
                            window_title='Transaction Details',
                            object_id="message_box"
                        )
                if event.ui_element == closeButton:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        PageManager.show_user_page(retrieved_user)

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        logo =gui.createImage(window, 50, 50, 75, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    alerts()
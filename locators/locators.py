from selenium.webdriver.common.by import By


class HeaderPageLocators:

    constructor_btn = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")                            
    order_feed_btn = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")                           
    personal_account_btn = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")                    


class MainPageLocators:

    order_feed_form = (By.XPATH, ".//div[@class = 'OrderFeed_orderFeed__2RO_j']")                    
    constructor_form = (By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']") 
    place_order_button = (By.XPATH, ".//button[text() = 'Оформить заказ']")                          
    fluorescent_bun_btn = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")                  
    close_popup_form = (By.XPATH, '//button[contains(@class,"close")]')                              
    counter_ingredient = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")         
    order_form = (By.XPATH, ".//div[@class = 'Modal_modal__container__Wo2l_']")                      
    order_basket = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")             
    order_num = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")            
    personal_account_btn = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")              
    popup_form_ingredients = (By.XPATH, "//h2[text()= 'Детали ингредиента']")                         


class AuthPageLocators:
    
    auth_form = (By.XPATH, ".//div[@class = 'Auth_LOGIN_ENDPOINT__3hAey']")                                   
    email_input = (By.XPATH, ".//input[@name = 'name']")                                             
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")                                        
    LOGIN_ENDPOINT_account_btn = (By.XPATH, "//button[text() = 'Войти']")                                     
    registration_btn = (By.XPATH, "//a[text() = 'Зарегистрироваться']")                              
    recover_btn = (By.XPATH, "//a[text() = 'Восстановить пароль']")                                  


class RecoveryPageLocators:

    email_input = (By.XPATH, ".//input[@name = 'name']")                                             
    recover_btn = (By.XPATH, ".//button[text() = 'Восстановить']")                                   
    LOGIN_ENDPOINT_account_btn = (By.XPATH, ".//a[text() = 'Войти']")                                         
    password_input = (By.XPATH, ".//input[@name = 'Введите новый пароль']")                          
    code_from_mail = (By.XPATH, ".//label[text() = 'Введите код из письма']")                        
    save_btn = (By.XPATH, ".//button[text() = 'Сохранить']")                                         
    recovery_text_form = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")                       
    show_btn = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")                       
    input_field_active = (By.CSS_SELECTOR, ".input.input_status_active")                             


class PersonalAreaLocators:

    profile_form = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")                           
    profile_btn = (By.XPATH, ".//a[text() = 'Профиль']")                                             
    order_history_btn = (By.XPATH, ".//a[text() = 'История заказов']")                               
    history_order_form = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")                  
    number_order = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")                  
    cancel_btn = (By.XPATH, ".//button[text() = 'Отмена']")                                          
    save_btn = (By.XPATH, ".//button[text() = 'Сохранить']")                                         
    exit_btn = (By.XPATH, ".//button[text() = 'Выход']")                                             


class OrderFeedLocators:

    title_orders_list = (By.XPATH, '//h1[text()="Лента заказов"]')                                 
    orders_info = (By.XPATH, '//p[text()="Cостав"]')                                               
    total_orders_counter = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    daily_orders_counter = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    number_order_in_job = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")     
    order_info_window = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")
    order_history = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')
    
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException
import re

# Inicialización el driver de Chrome usando webdriver_manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def click_button(driver, selector, by=By.CSS_SELECTOR, wait_time=10):
    try:
        button = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((by, selector))
        )
        button.click()
        print(f"✅ Botón con selector '{selector}' clickeado exitosamente.")
        return True
    except TimeoutException:
        print(f"❌ Error: El botón con selector '{selector}' no se volvió clickeable en {wait_time} segundos.")
        return False
    except ElementClickInterceptedException:
        print(f"❌ Error: Otro elemento interceptó el clic en el botón con selector '{selector}'.")
        # Aquí podrías intentar hacer scroll o esperar un poco más si es un pop-up, por ejemplo.
        return False
    except NoSuchElementException:
        print(f"❌ Error: El botón con selector '{selector}' no fue encontrado.")
        return False
    except Exception as e:
        print(f"⚠️ Error inesperado al intentar clickear el botón con selector '{selector}': {e}")
        return False
    

# Definición de la URL a la que quieres acceder
url = "https://backoffice.nilus.co/es-AR/login"
pedido = "https://backoffice.nilus.co/es-AR/orders/ce3a967c-0c2a-4765-8412-60363c953469"

try:
    # Abre la URL en el navegador
    driver.get(url)
    time.sleep(5)
    campo_email = driver.find_element(By.ID, "email")
    campo_email.send_keys("juan.silva96@hotmail.com")
    # Opcional: Agrega un pequeño tiempo de espera para que la página cargue completamente
    campo_contraseña = driver.find_element(By.ID, "password")
    campo_contraseña.send_keys("contrasenaponer")
    time.sleep(5)
    selector_ingresar_xpath = "//button[text()='INGRESAR']"
    if click_button(driver, selector_ingresar_xpath, by=By.XPATH):
        print("Se hizo clic en el botón INGRESAR usando XPath.")
    else:
        print("No se pudo hacer clic en el botón INGRESAR usando XPath.")
    time.sleep(10)
    driver.get(pedido)
    time.sleep(5)
    nombre_producto_buscado = "Queso untable ILOLAY Jamon 190 gr"
    # Espera a que los productos estén visibles
    productos = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "css-1es96wk"))
    )
    for producto in productos:
        nombre = producto.find_element(By.TAG_NAME, "span").text.strip()
        if nombre == nombre_producto_buscado:
            boton_svg = producto.find_element(By.CSS_SELECTOR, 'svg[data-testid="DoNotDisturbOnIcon"]')

            # Scroll para asegurarse que el SVG esté visible
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton_svg)

            try:
                # Intentar click normal
                boton_svg.click()
                time.sleep(5)
            except Exception as e:
                print(f"Click normal falló por {e}, intentando con JavaScript")
                # Click con JS como fallback
                driver.execute_script("arguments[0].click();", boton_svg)

            print(f"Click realizado en DoNotDisturbOnIcon de '{nombre_producto_buscado}'")
            break
    else:
        print(f"No se encontró el producto '{nombre_producto_buscado}'")

    click_button(driver, '//div[@role="combobox" and @id="reason"]', by=By.XPATH)
    time.sleep(5)
    
    try:
        opcion_motivo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//li[contains(text(), "Support - DTC - Operations - Missing Product")]'))
    )
        opcion_motivo.click()
        print("✅ Opción 'Support - DTC - Operations - Missing Product' seleccionada exitosamente.")
    except Exception as e:
        print(f"❌ No se pudo seleccionar la opción del motivo: {e}")
    time.sleep(5)
       
    cantidad_deseada = "1"

    try:
        input_cantidad = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "quantity"))
        )
        input_cantidad.clear()  # Limpia el valor anterior (0)
        input_cantidad.send_keys(cantidad_deseada)
        print(f"✅ Se ingresó la cantidad '{cantidad_deseada}' correctamente.")
    except Exception as e:
        print(f"❌ No se pudo ingresar la cantidad: {e}")
    time.sleep(5)

    try:
        boton_solicitar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Solicitar']"))
            )
        boton_solicitar.click()
        print("✅ Se hizo clic en el botón 'Solicitar' exitosamente.")
    except Exception as e:
        print(f"❌ No se pudo hacer clic en 'Solicitar': {e}")
    time.sleep(5)

    try:
        boton_guardar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Guardar cambios']"))
        )
        boton_guardar.click()
        print("✅ Se hizo clic en el botón 'Guardar cambios' exitosamente.")
    except Exception as e:
        print(f"❌ No se pudo hacer clic en 'Guardar cambios': {e}")
    time.sleep(100)                                


except Exception as e:
        print(f"Ocurrió un error: {e}")               
finally:
    # Cierra el navegador al finalizar, independientemente de si hubo un error o no
    driver.quit()

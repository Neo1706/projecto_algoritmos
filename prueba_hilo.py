import threading

class MiHilo(threading.Thread):
    def run(self):
        # Código a ejecutar en el hilo
        print("Hola desde el hilo")
        # Algoritmo de Library Sort

        def binary_search_with_whitespace(arr, target):
            # Sort the array with whitespace preserved
            sorted_arr = sorted(arr, key=lambda x: x.strip())

            # Perform binary search
            left = 0
            right = len(sorted_arr) - 1

            while left <= right:
                mid = (left + right) // 2
                mid_value = sorted_arr[mid].strip()

                if mid_value == target:
                    return mid
                elif mid_value < target:
                    left = mid + 1
                else:
                    right = mid - 1

            # If target is not found, find similar elements
            similar_elements = []
            for element in sorted_arr:
                if target in element:
                    similar_elements.append(element)

            if similar_elements:
                print(f"'{target}' not found. Similar elements: {similar_elements}")
            else:
                print(f"'{target}' not found.")

            return -1

        # Example usage
        arr = ["apple", " banana", "cherry", "  date", "  elderberry",""]
        target = "dat"

        index = binary_search_with_whitespace(arr, target)
        if index != -1:
            print(f"Found '{target}' at index {index}")
            print(f"Original array: {arr}")
            print(f"Sorted array: {sorted(arr, key=lambda x: x.strip())}")

        else:
            print(f"'{target}' not found")

        

# Crear un objeto de la clase MiHilo
hilo = MiHilo()

# Iniciar el hilo
hilo.start()

# Esperar a que el hilo termine
hilo.join()

print("Hilo terminado")

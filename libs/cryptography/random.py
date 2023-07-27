import binascii
import requests
import random

class Random():
    def quantum(self):
        seed = self._get_random_seed()
        if seed: random.seed(seed)

    def choice(self, array):
        return random.choice(array)

    def shuffle(self, array):
        return random.shuffle(array)

    def _get_random_seed(self):
        try:
            response = requests.get("https://qrng.anu.edu.au/wp-content/plugins/colours-plugin/get_block_hex.php")

            if response.ok:
                seed = binascii.a2b_hex(response.text)
                if seed:
                    return seed
                else:
                    print("Error: No 'data' field in the API response.")
            else:
                print(f"Error: Unable to fetch random seed from API. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: Unable to connect to the API. {e}")
        return None
    
    # def _read_seed_from_cache(self):
    #     try:
    #         with open("", "rb") as file:
    #             encrypted_seed = file.read()
    #             decrypted_seed = self._cipher.decrypt(encrypted_seed)
    #             return decrypted_seed
    #     except FileNotFoundError:
    #         return None
    #     except Exception as e:
    #         print(f"Error: Unable to read seed from cache. {e}")
    #         return None
        
    # def _save_seed_to_cache(self, seed):
    #     try:
    #         encrypted_seed = self._cipher.encrypt(seed)
    #         with open("CACHE_FILE", "wb") as file:
    #             file.write(encrypted_seed)
    #     except Exception as e:
    #         print(f"Error: Unable to save seed to cache. {e}")
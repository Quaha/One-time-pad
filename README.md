# [EN] One-time pad
### What kind of program is this?
**One-time pad** is a program for encrypting and decrypting text messages using the [disposable notepad method](https://en.wikipedia.org/wiki/One-time_pad). The first version of the program 1.0 was released on 07/18/2021.

### How does it work?
After entering the message, the program generates an encryption key, the size of which matches the size of the text. This is done using the [secrets](https://docs.python.org/3/library/secrets.html) module. The message is then encrypted using the [Vigener cipher](https://en.wikipedia.org/wiki/Vigenère_cipher ).

### Is it safe to encrypt data?
The encryption method itself has [absolute cryptographic strength](https://en.wikipedia.org/wiki/Strong_cryptography ), since there are an infinite number of keys for a specific encrypted text that can decrypt it into absolutely any message. Security problems can only arise either when transmitting an encrypted message and a key (which is exclusively a problem for the program user), or when generating a key using the **secrets** module, however, since it is sufficiently *secure*, this problem disappears.

(The safety of the module is written in the [official documentation](https://docs.python.org/3/library/secrets.html ) according to it in the first paragraph, if you think that this is not the case, you can replace this module with another one)

### History of creation
This program was created while learning the **Python** language in the summer of 2021 in the book "Cryptography and hacking in Python".

>Sweigart A. Cracking codes with Python: an introduction to building and breaking ciphers. – No Starch Press, 2018.

---

# [RU] One-time pad — одноразовый шифроблокнот
### Что это за программа?
**One-time pad** — программа для шифрования и дешифрования текстовых сообщений методом [одноразового блокнота](https://en.wikipedia.org/wiki/One-time_pad). Первая версия программы v1.0 была выпущена 18.07.2021.

### Как она работает?
После ввода сообщения программа генерирует ключ шифрования, размер которого совпадает с размером текста. Это происходит с помощью модуля [secrets](https://docs.python.org/3/library/secrets.html). Затем сообщение шифруется с помощью [шифра Виженера](https://en.wikipedia.org/wiki/Vigenère_cipher).

### Безопасно ли ей шифровать данные?
Сам метод шифрования обладает [абсолютной криптографической стойкостью](https://en.wikipedia.org/wiki/Strong_cryptography), так как для конкретного зашифрованного текста существует бесконечное множество ключей, которые могут расшифровать его в совершенно любые сообщения. Проблемы безопасности могут возникнуть лишь или при передаче зашифрованного сообщения и ключа (что является исключительно проблемой пользователя программы), или при генерации ключа с помощью модуля **secrets**, однако, так как он является достаточно *безопасным*, эта проблема отпадает.

(О безопасности модуля написано в [официальной документации](https://docs.python.org/3/library/secrets.html) по нему в первом абзаце, если считаете, что это не так, можете заменить этот модуль на другой)

### История создания
Данная программа была создана во время изучения языка **Python** летом 2021 года по книге "Криптография и взлом шифров на Python".

>Sweigart A. Cracking codes with Python: an introduction to building and breaking ciphers. – No Starch Press, 2018.

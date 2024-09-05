import re
def PasswordStrengthChecker(self, password):
        # basic password identification
        error = []
        is_strong = False
        atoz = "abcdefghijklmnopqrstuvwxyz"
        qtop = "qwertyuiop"
        atol = "asdfghjkl"
        ztom = "zxcvbnm"
        special_chars = "!@#$%^&*()_+=-"
        zerotonine = "0123456789"
        is_lAlpha_correct = True
        is_uAlpha_correct = True
        is_digit_correct = True
        is_spChar_correct = True

        # check whether the password contains at least one lowercase alphabet
        # G7f$k8!z
        # G7f$k8ac
        if len(password) >= 8:
            if (re.search(r"[a-z]+", password) is None) or (re.search(r"[A-Z]+", password) is None) or (
                    re.search(r"[0-9]+", password) is None) or (re.search(r"[!@#$%^&*()_+=-]+", password) is None):
                print("password must contain at least one lowercase alphabet, one uppercase alphabet, "
                      "one number or at least one special character")
            elif re.match(r"^(?!.*[0-9]{2})(?!.*[a-z]{2})(?!.*[A-Z]{2})(?!.*[!@#$%^&*()_+=]{2}).{8}$", password):
                is_strong = True
            else:
                lower_alpha = re.findall(r"[a-z]{2}", password)
                upper_alpha = re.findall(r"[A-Z]{2}", password)
                digits = re.findall(r"[0-9]{2}", password)
                special_characters = re.findall(r"[!@#$%^&*()=+_-]{2}", password)

                if len(lower_alpha) != 0:
                    for i in lower_alpha:
                        if (i in atoz) or (i in qtop) or (i in atol) or (i in ztom):
                            is_lAlpha_correct = False
                            is_strong = False
                            error.append("Please do not enter non consecutive sequence of lowercase letters")
                        else:
                            is_lAlpha_correct = True
                            is_strong = True

                if len(upper_alpha) != 0:
                    for i in upper_alpha:
                        if i in atoz.upper() or i in qtop.upper() or i in atol.upper() or i in ztom.upper():
                            is_uAlpha_correct = False
                            error.append("Please do not enter non consecutive sequence of uppercase letters")
                            break
                        else:
                            is_uAlpha_correct = True
                            is_strong = True

                if len(digits) > 0:
                    for i in digits:
                        if i in zerotonine:
                            is_digit_correct = False
                            error.append("Please do not enter non consecutive sequence of numbers")
                            is_strong = False
                            break
                        else:
                            is_digit_correct = True
                            is_strong = True

                if len(special_characters) != 0:
                    for i in special_characters:
                        if i in special_chars:
                            is_spChar_correct = False
                            error.append("Please do not enter non consecutive sequence of characters")
                            is_strong = False
                            break
                        else:
                            is_spChar_correct = True
                            is_strong = True

                if (is_lAlpha_correct is True) and (is_uAlpha_correct is True) and (is_digit_correct is True) and (is_spChar_correct is True):
                    is_strong = True
                    print(is_strong)
                    print(password, " is strong password")
                else:
                    is_strong = False
                    print(error)
                    print(password, " is weak password")
        else:
            print("Password must have at least 8 characters")
        # check if no sequential special characters.

PasswordStrengthChecker("kook@RF1")

def main():
    ##################################################
    # Comlete your code here
    str = 'Python Programming'
    sub1 = str[:6]
    sub2 = str[-11:]
    sub3 = sub2 + ' ' + sub1
    print(f'{sub2}\n{sub1}\n{sub3}')
    # print(f'{str[-11:]}\n{str[:6]}\n{str[-11:]} {str[:6]}')     #### Alternative only using one variable
    ##################################################
    pass


if __name__ == '__main__':
    main()

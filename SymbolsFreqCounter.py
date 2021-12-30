text1 = "схема системы  приведена на ри " 
text2 = " сущность этой угрозы состоит в том что если злоумышленник получит ключ шифрования то он может пытаться восстановить значения  использованные в предыдущих транзакциях  сущность этой угрозы состоит в том что если злоумышленник получит ключ шифрования то он попытается восстановить значения  которые будут использоваться в последующих транзакциях для защиты от угроз обратного и прямого  схема системы  приведена на рис  покупатель для оплаты покупки предъявляет свою дебетовую или кредитную карту и вводит значение  для подтверждения личности продавец в свою очередь вводит сумму денег которую необходимо уплатить за покупку или услуги затем в банкэквайер банк продавца направляется запрос на перевод денег банкэквайер переадресует этот запрос в банкэмитент для проверки подлинности карты предъявленной покупателем если эта карта подлинная и покупатель имеет право применять ее для оплаты продуктов и услуг банкэмитент переводит деньги в банкэквайер на счет продавца после перевода денег на счет продавца банкэквайер посылает на терминал извещение в котором сообщает о завершении транзакции после этого продавец выдает покупателю товар и извещение следует обратить внимание на тот сложный путь который должна проделать информация о покупке прежде чем будет осуществлена транзакция во время прохождения этого пути возможны искажения и потеря сообщений для защиты системы  должны выполняться следующие требования проверка  введенного покупателем должна производиться системой банкаэмитента при пересылке "

def CountSymbolsFreq(inputText: str):
    voc = sorted(''.join(set(inputText)))
    textLength = len(inputText)
    freqDict = {}
    for elem in voc:
        freqDict[elem] = round(inputText.count(elem) / textLength, 3)
    del textLength
    del voc

    return freqDict


freqs1 = CountSymbolsFreq(text1)
print('Частоты первого текста:\n', freqs1)

freqs2 = CountSymbolsFreq(text2)
print('Частоты второго текста:\n', freqs2)


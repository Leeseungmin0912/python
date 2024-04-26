#컨테이너 종류 - 튜플() 리스트[] 딕셔너리{} 셋{}
#딕셔너리{} 키:값
person = {
    '이름':'이승민', 
          '나이':17,
            '키':'170',
          '집주소':'부평구 산곡동'}
print(person['이름'])
print(person)
person['몸무게'] = 60
person['키'] = 180
print(person)
del person['나이']
print(person)
print(person.get('집수소'))

print("나이" in person)
print("이름" in person)
print("이름" in person.values())

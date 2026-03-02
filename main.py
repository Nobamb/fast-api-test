import asyncio
import time

# 3개의 비동기 작업을 정의해 볼게 (네트워크 요청이라고 상상해 봐)
async def worker(name, delay_time):
    print(f"[{name}] 작업 시작! (예상 시간: {delay_time}초)")
    
    # 여기서 제어권을 이벤트 루프에게 던짐! (JS의 await fetch()와 동일)
    await asyncio.sleep(delay_time) 
    
    print(f"[{name}] 작업 완료! 🎉")

async def main():
    print("=== 메인 이벤트 루프 시작 ===")
    
    # JS의 Promise.all()과 완벽하게 똑같은 역할이야!
    # 3개의 코루틴을 이벤트 루프(함수 외부)에 동시에 던져버려.
    await asyncio.gather(
        worker("A", 3),  # 3초 걸림
        worker("B", 1),  # 1초 걸림
        worker("C", 2)   # 2초 걸림
    )
    
    print("=== 모든 작업 끝! 메인 종료 ===")

# ---------------------------------------------------------
# 엔진 선택하기! (여기서 기본이냐 uvloop냐가 결정돼)
# ---------------------------------------------------------

if __name__ == "__main__":
    start_time = time.time()
    
    # 1. 기본 파이썬 엔진(asyncio)으로 실행할 때:
    asyncio.run(main())
    
    # 2. 만약 uvloop(Uvicorn 엔진)로 실행하고 싶다면 위 코드 대신 이렇게 써:
    # import uvloop
    # uvloop.install()  <-- "지금부터 기본 엔진 빼고 페라리 엔진으로 교체해!" 라는 뜻
    # asyncio.run(main())
    
    print(f"총 걸린 시간: {time.time() - start_time:.2f}초")
    # 기본 파이썬 동작
    #     === 메인 이벤트 루프 시작 ===
    # [A] 작업 시작! (예상 시간: 3초)
    # [B] 작업 시작! (예상 시간: 1초)
    # [C] 작업 시작! (예상 시간: 2초)
    # [B] 작업 완료! 🎉
    # [C] 작업 완료! 🎉
    # [A] 작업 완료! 🎉
    # === 모든 작업 끝! 메인 종료 ===
    # 총 걸린 시간: 3.02초
    # [A] 작업 시작! (예상 시간: 3초)
    # [B] 작업 시작! (예상 시간: 1초)
    # [C] 작업 시작! (예상 시간: 2초)
    # [B] 작업 완료! 🎉
    # [C] 작업 완료! 🎉
    # [A] 작업 완료! 🎉
    # === 모든 작업 끝! 메인 종료 ===
    # 총 걸린 시간: 3.03초
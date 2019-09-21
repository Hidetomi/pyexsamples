# pyexsamples

## 疑問

Timerスレッド内で新しいスレッドを生成・起動してるので、sys.exit()をコールしてもメインプロセスが終わらない。  
正直sys.exit()で全てのスレッドは強制的に終了される（killされる）と思ってたけどそこまでの影響力はない！？  

## 実行結果

```bash
main
timer thread start
thread status => [<Timer(Thread-6, started 3856)>]
thread status => [<Timer(Thread-8, initial)>]
timer thread start < child thread
thread status => [<Timer(Thread-6, stopped 3856)>]
thread status => [<Timer(Thread-8, started 8316)>]
thread status => [<Timer(Thread-10, initial)>]
timer thread start < child thread
thread status => [<Timer(Thread-6, stopped 3856)>]
thread status => [<Timer(Thread-8, stopped 8316)>]
thread status => [<Timer(Thread-10, started 8672)>]
thread status => [<Timer(Thread-12, initial)>]
timer thread start < child thread
thread status => [<Timer(Thread-6, stopped 3856)>]
thread status => [<Timer(Thread-8, stopped 8316)>]
thread status => [<Timer(Thread-10, stopped 8672)>]
thread status => [<Timer(Thread-12, started 6372)>]
thread status => [<Timer(Thread-14, initial)>]
timer thread start < child thread
thread status => [<Timer(Thread-6, stopped 3856)>]
thread status => [<Timer(Thread-8, stopped 8316)>]
thread status => [<Timer(Thread-10, stopped 8672)>]
thread status => [<Timer(Thread-12, stopped 6372)>]
thread status => [<Timer(Thread-14, started 10808)>]
thread status => [<Timer(Thread-16, initial)>]
timer thread start < child thread
thread status => [<Timer(Thread-6, stopped 3856)>]
thread status => [<Timer(Thread-8, stopped 8316)>]
thread status => [<Timer(Thread-10, stopped 8672)>]
thread status => [<Timer(Thread-12, stopped 6372)>]
thread status => [<Timer(Thread-14, stopped 10808)>]
thread status => [<Timer(Thread-16, started 1144)>]
thread status => [<Timer(Thread-18, initial)>]
timer thread start < child thread
exit main process.
thread status => [<Timer(Thread-6, stopped 3856)>]
thread status => [<Timer(Thread-8, stopped 8316)>]
thread status => [<Timer(Thread-10, stopped 8672)>]
thread status => [<Timer(Thread-12, stopped 6372)>]
thread status => [<Timer(Thread-14, stopped 10808)>]
thread status => [<Timer(Thread-16, stopped 1144)>]
thread status => [<Timer(Thread-18, started 9860)>]
thread status => [<Timer(Thread-20, initial)>]
timer thread start < child thread

...
```

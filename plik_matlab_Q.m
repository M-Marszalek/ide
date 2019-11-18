x = 0.01;
a = 1;

for k = 1:100
    sim('mojschemat.slx', 100);
    et = simout.data;
    et2 = et.*et;
    t = (simout.time);
    t2 = t.^ (-simout.data);
    w = et2 + t2;
    Q(a) = trapz(simout.time, w);
    x = x + 0.01;
    a = a + 1;
end

[A B] = min(Q)
Q_wynik = Q(B)
disp(Q_wynik)
disp(B)
colnames(mtcars)
dim(mtcars)
cor(mtcars[1:4])

modelo = lm(mpg ~ disp, data=mtcars)

summary(modelo)$r.squared
summary(modelo)$adj.r.squared

plot(mpg ~ disp, data=mtcars)
abline(modelo)

predict(modelo, data.frame(disp=200))

modelo = lm(mpg ~ disp + hp + cyl, data=mtcars)
summary(modelo)$r.squared
summary(modelo)$adj.r.squared

predict(modelo, data.frame(disp=200, hp=100, cyl=4))
 
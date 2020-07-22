from Gaussiandistribution import Gaussian

gaussian_one = Gaussian(20, 2)

gaussian_two = Gaussian(19, 4)

gaussian_three = gaussian_one + gaussian_two

print(gaussian_three.stdev)
print(gaussian_three.mean)
# EXERCISE 3 : Use of ML Models

In this exercise, we are going to see how to use our model, meaning creating it, training it, saving it on disk, loading it and using it on new data.

There is a difference between training and using a model.

***Using*** a model means providing inputs and receiving an estimation/prediction as output. This process takes less than a few seconds, and only **features** are needed as input data.

***Training*** a model is the process of improving how well a model works. This requires to use the model, objective function and optimizer in sepcific order and can take several days to complete. We only need to train the model **ONCE**. 
Once it is trained, we can use it as many times as we want. During training we need both the ***features*** (input data) and ***labels*** (correct answer). 

It's common to build, train, then use a model while we're just learning about machine learning; but in the real world, we don't want to train the model every time we want to make a prediction.

Consider our avalanche-dog equipment store scenario:

We want to train the model just once, then load that model onto the server that runs our online store.
Although the model is trained on a dataset we downloaded from the internet, we actually want to use it to estimate the boot size of our customers' dogs who aren't in this dataset!
How can we do this?

- Create a basic model.
- Save it to disk.
- Load it from disk.
- Use it to make predictions about a dog who was not in the training dataset.

const one = () => {
    console.log('one');
}

const two = async () => {
    await setTimeout(() => {
        console.log('I was waiting for someone!');
    }, 2000);
    console.log('two');
}

const three = () => {
    console.log('three');
}

one();
two();
three();
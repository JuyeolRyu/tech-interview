import produce from 'immer';
const coke = {
    name: 'coca',
    fake: {
        name: 'pepsi',
    }
}

const new_coke = produce(coke, (draft) => {
    draft.name = 'pepsi';
    draft.fake.name = 'coca';
});
console.log(coke);
console.log(new_coke);
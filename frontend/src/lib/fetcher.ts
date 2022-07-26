const api_key = import.meta.env.VITE_API_KEY;

async function getFetcher(url: string) {
    const res = await fetch(url, {
        method: "GET",
        mode: "cors",
        headers: {
            Authorization: api_key,
        },
    });
    const data = await res.json();
    // console.log(data);
    if (res.ok) {
        return data;
    } else {
        throw new Error(data);
    }
}

export default getFetcher;

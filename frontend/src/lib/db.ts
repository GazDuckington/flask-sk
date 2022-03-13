export async function predictText(url, data) {
    const load = async () => {}
    const res = await fetch(url, {
        method: 'POST',
        body: JSON.stringify({"data": data}),
        headers: {
            "Content-type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    });
    const hasil = await res.json();

    if (res.ok) { return hasil }
    else { throw new Error(hasil) }
}
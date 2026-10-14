// Gecikmeli ve sıralı otomatik kayıt. Kayıtlar üst üste binmez; son veri her zaman yazılır.

export function createAutosave({ delay = 600, save, onState } = {}) {
  let timer = null;
  let pending = null;
  let hasPending = false;
  let chain = Promise.resolve();
  let lastError = null;

  function setState(state, extra) {
    if (onState) onState(state, extra);
  }

  function run() {
    timer = null;
    if (!hasPending) return chain;
    const data = pending;
    hasPending = false;
    pending = null;
    setState('saving');
    chain = chain
      .then(() => save(data))
      .then((result) => {
        lastError = null;
        if (!hasPending) setState('saved', result);
        return result;
      })
      .catch((err) => {
        lastError = err;
        setState('error', err);
      });
    return chain;
  }

  return {
    schedule(data) {
      pending = data;
      hasPending = true;
      setState('dirty');
      if (timer) clearTimeout(timer);
      timer = setTimeout(run, delay);
    },
    async flush() {
      if (timer) {
        clearTimeout(timer);
        timer = null;
      }
      await run();
      await chain;
      if (lastError) throw lastError;
    },
    cancel() {
      if (timer) clearTimeout(timer);
      timer = null;
      hasPending = false;
      pending = null;
    },
    get isPending() {
      return hasPending || timer !== null;
    }
  };
}
